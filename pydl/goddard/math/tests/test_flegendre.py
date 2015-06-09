# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-
import pytest
#
def test_flegendre():
    from .. import flegendre
    import numpy as np
    x = np.array([-1,-0.5,0,0.5,1],dtype='d')
    #
    # Test order
    #
    with pytest.raises(ValueError):
        f = flegendre(x,0)
    #
    # m = 1
    #
    f = flegendre(x,1)
    assert (f == np.ones((1,x.size),dtype='d')).all()
    #
    # m = 2
    #
    f = flegendre(x,2)
    foo = np.ones((2,x.size),dtype='d')
    foo[1,:] = x
    assert np.allclose(f,foo)
    #
    # m = 3
    #
    f = flegendre(x,3)
    foo = np.ones((3,x.size),dtype='d')
    foo[1,:] = x
    foo[2,:] = 0.5*(3.0*x**2 - 1.0)
    assert np.allclose(f,foo)
    #
    # m = 4
    #
    f = flegendre(x,4)
    foo = np.ones((4,x.size),dtype='d')
    foo[1,:] = x
    foo[2,:] = 0.5*(3.0*x**2 - 1.0)
    foo[3,:] = 0.5*(5.0*x**3 - 3.0*x)
    assert np.allclose(f,foo)
    #
    # random float
    #
    f = flegendre(2.88,3)
    assert np.allclose(f,np.array([[1.00], [2.88], [11.9416]]))
