# Mathematical Formulation

For input frame `x_t`, encoder `E_theta` gives `z_t = E_theta(x_t)`. Segmentation probabilities are `p_t = softmax(S_phi(z_t))`. A temporal predictor `F_psi` predicts `z_hat_t = F_psi(z_(t-k:t-1))`.

A possible source training objective is:
`L_source = L_seg + lambda_pred L_pred`,
where `L_seg` is pixel-wise cross-entropy (and optionally class-weighted) and `L_pred = 1 - cosine(z_t, z_hat_t)` or a normalized smooth-L1 loss.

For semantic histogram `h_t(c) = mean_pixels p_t(c)`, define:
`d_s(t) = JS(h_t || h_source)`.
For predictive surprise:
`d_p(t) = mean(1 - cosine(z_t, z_hat_t))`.
For feature shift:
`d_f(t) = distance(mu_target, mu_source)` using a fixed, documented feature layer and distance estimator.

After robust normalization, fuse:
`D_t = w_f q_f(t) + w_s q_s(t) + w_p q_p(t) + w_u q_u(t)`.
The weights and threshold are selected on validation data only.

For selected pixels `Omega_t`, an adaptation loss may be:
`L_TTA = mean_{i in Omega_t} H(p_t(i)) + lambda_cons L_consistency`.
This objective is only a candidate. Compare with published TTA methods and include an ablation without adaptation.
