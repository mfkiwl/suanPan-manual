# SimpleSand

A Simple Sand Model

The continuum mechanics based sign convention (tension is positive) is used for consistency.

The `SimpleSand` model is a simple sand hardening model that adopts a bounding surface concept.

Readers can also refer to the corresponding section
in [Constitutive Modelling Cookbook](https://github.com/TLCFEM/constitutive-modelling-cookbook/releases/download/latest/COOKBOOK.pdf)
for details on the theory.

## Syntax

```
material SimpleSand (1) (2) (3) (4) (5) (6) (7) (8) (9) (10) (11) (12) (13) [14]
# (1) int, unique material tag
# (2) double, elastic modulus
# (3) double, poissons ratio
# (4) double, m, size of yield surface
# (5) double, A, dilatancy related parameter, often negative
# (6) double, h, dilatancy related hardening parameter
# (7) double, alpha_c, critical alpha
# (8) double, n_b, bounding surface evolution parameter
# (9) double, n_d, dilatancy surface evolution parameter
# (10) double, v_c, critical specific volume
# (11) double, p_c, critical hydrostatic stress, should be negative
# (12) double, lambda_c, the slope of critical state line
# (13) double, v_0, initial specific volume
# [14] double, density, default: 0.0
```

## Theory

### Critical State

The state parameter is defined as

$$
\psi=v-v_c+\lambda_c\ln\left(\dfrac{p}{p_c}\right)
$$

The specific volume can be expressed in terms of strain,

$$
v=v_0\left(1+\mathrm{tr}~\varepsilon\right).
$$

Thus, the bounding surface and dilatancy surface can be defined to evolve with $$\psi$$,

$$
\alpha^b=\alpha^c\exp\left(-n^b\psi\right),\qquad \alpha^d=\alpha^c\exp\left(n^d\psi\right),
$$

where $$\alpha^c$$ is the initial size of surfaces.

### Yield Surface

The following wedge-like function is chosen to be the yield surface,

$$
F=|s+p\alpha|+mp,
$$

where $$s$$ is the deviatoric stress, $$p$$ is the hydrostatic stress, $$\alpha$$ is the back stress ratio and $$m$$ is
a constant that controls the size of the wedge.

### Flow Rule

A non-associated flow rule is defined.

$$
\Delta\varepsilon^p=\Delta\gamma{}\left(n+\dfrac{1}{3}DI\right),
$$

where $$n=\dfrac{s+p\alpha}{|s+p\alpha|}$$ is a unit tensor, $$I$$ is the second order unit tensor and $$D=A\left(
\alpha^d-\alpha:n\right)$$ is the dilatancy parameter.

Note due to the change of sign convention, a negative $$D$$ leads to contractive response, thus $$A$$ often needs to be
negative.

### Hardening Rule

The evolution of $$\alpha$$ is similar to the Armstrong-Frederick hardening law.

$$
\Delta\alpha=\Delta\gamma{}h\left(\alpha^bn-\alpha\right),
$$

where $$h$$ is a constant that controls the speed of hardening.

## Example

Please refer to [triaxial-compression-of-sand](../../../../Example/Geotechnical/triaxial-compression-of-sand.md).