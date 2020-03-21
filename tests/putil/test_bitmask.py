from panda3d import core
import pickle


def test_bitmask_allon():
    assert core.BitMask16.all_on().is_all_on()
    assert core.BitMask32.all_on().is_all_on()
    assert core.BitMask64.all_on().is_all_on()
    assert core.DoubleBitMaskNative.all_on().is_all_on()
    assert core.QuadBitMaskNative.all_on().is_all_on()


def test_bitmask_nonzero():
    assert not core.BitMask16()
    assert not core.BitMask32()
    assert not core.BitMask64()
    assert not core.DoubleBitMaskNative()
    assert not core.QuadBitMaskNative()


def test_bitmask_getstate():
    assert core.BitMask32().__getstate__() == 0
    assert core.BitMask32(12345).__getstate__() == 12345


def test_bitmask_pickle():
    assert pickle.loads(pickle.dumps(core.BitMask16(0), -1)).is_zero()

    mask1 = core.BitMask16(123)
    data = pickle.dumps(mask1, -1)
    mask2 = pickle.loads(data)
    assert mask1 == mask2
