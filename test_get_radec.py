import numpy
def test_get_radec():
    import sky_sim
    answer = (14.215420962967535, 41.26916666666667)
    result = sky_sim.get_radec()
    numpy.testing.assert_allclose(answer, result, atol=1./3600)