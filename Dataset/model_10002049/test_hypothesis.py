import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Menghapus_Nilai_external,
    Menghapus_Mahasiswa_external,
    Mengubah_Data_Nilai_external,
    Mengubah_Data_Mahasiswa_external,
    Menambah_Data_Nilai_external,
    Menambah_Data_Mahasiswa_external,
    Melihat_Data_Nilai_external,
    Melihat_Data_Mahasiswa_external,
    Activity_Input_Mahasiswa,
    Activity_Data_Nilai,
    Activity_Data_Mahasiswa,
    view_control_Nilai,
    view_control_Mahasiswa,
    DAO_Nilai,
    DAO_Mahasiswa,
    Aplikasi_Input_Nilai_Matakuliah_Component,
    Dosen_Actor,
    Nilai,
    Mahasiswa,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_menghapus_nilai_external_is_not_abstract():
    assert not inspect.isabstract(Menghapus_Nilai_external)


def test_menghapus_nilai_external_constructor_exists():
    assert callable(Menghapus_Nilai_external.__init__)


def test_menghapus_nilai_external_constructor_args():
    sig = inspect.signature(Menghapus_Nilai_external.__init__)
    params = list(sig.parameters.keys())



def test_menghapus_mahasiswa_external_is_not_abstract():
    assert not inspect.isabstract(Menghapus_Mahasiswa_external)


def test_menghapus_mahasiswa_external_constructor_exists():
    assert callable(Menghapus_Mahasiswa_external.__init__)


def test_menghapus_mahasiswa_external_constructor_args():
    sig = inspect.signature(Menghapus_Mahasiswa_external.__init__)
    params = list(sig.parameters.keys())



def test_mengubah_data_nilai_external_is_not_abstract():
    assert not inspect.isabstract(Mengubah_Data_Nilai_external)


def test_mengubah_data_nilai_external_constructor_exists():
    assert callable(Mengubah_Data_Nilai_external.__init__)


def test_mengubah_data_nilai_external_constructor_args():
    sig = inspect.signature(Mengubah_Data_Nilai_external.__init__)
    params = list(sig.parameters.keys())



def test_mengubah_data_mahasiswa_external_is_not_abstract():
    assert not inspect.isabstract(Mengubah_Data_Mahasiswa_external)


def test_mengubah_data_mahasiswa_external_constructor_exists():
    assert callable(Mengubah_Data_Mahasiswa_external.__init__)


def test_mengubah_data_mahasiswa_external_constructor_args():
    sig = inspect.signature(Mengubah_Data_Mahasiswa_external.__init__)
    params = list(sig.parameters.keys())



def test_menambah_data_nilai_external_is_not_abstract():
    assert not inspect.isabstract(Menambah_Data_Nilai_external)


def test_menambah_data_nilai_external_constructor_exists():
    assert callable(Menambah_Data_Nilai_external.__init__)


def test_menambah_data_nilai_external_constructor_args():
    sig = inspect.signature(Menambah_Data_Nilai_external.__init__)
    params = list(sig.parameters.keys())



def test_menambah_data_mahasiswa_external_is_not_abstract():
    assert not inspect.isabstract(Menambah_Data_Mahasiswa_external)


def test_menambah_data_mahasiswa_external_constructor_exists():
    assert callable(Menambah_Data_Mahasiswa_external.__init__)


def test_menambah_data_mahasiswa_external_constructor_args():
    sig = inspect.signature(Menambah_Data_Mahasiswa_external.__init__)
    params = list(sig.parameters.keys())



def test_melihat_data_nilai_external_is_not_abstract():
    assert not inspect.isabstract(Melihat_Data_Nilai_external)


def test_melihat_data_nilai_external_constructor_exists():
    assert callable(Melihat_Data_Nilai_external.__init__)


def test_melihat_data_nilai_external_constructor_args():
    sig = inspect.signature(Melihat_Data_Nilai_external.__init__)
    params = list(sig.parameters.keys())



def test_melihat_data_mahasiswa_external_is_not_abstract():
    assert not inspect.isabstract(Melihat_Data_Mahasiswa_external)


def test_melihat_data_mahasiswa_external_constructor_exists():
    assert callable(Melihat_Data_Mahasiswa_external.__init__)


def test_melihat_data_mahasiswa_external_constructor_args():
    sig = inspect.signature(Melihat_Data_Mahasiswa_external.__init__)
    params = list(sig.parameters.keys())



def test_activity_input_mahasiswa_is_not_abstract():
    assert not inspect.isabstract(Activity_Input_Mahasiswa)


def test_activity_input_mahasiswa_constructor_exists():
    assert callable(Activity_Input_Mahasiswa.__init__)


def test_activity_input_mahasiswa_constructor_args():
    sig = inspect.signature(Activity_Input_Mahasiswa.__init__)
    params = list(sig.parameters.keys())



def test_activity_data_nilai_is_not_abstract():
    assert not inspect.isabstract(Activity_Data_Nilai)


def test_activity_data_nilai_constructor_exists():
    assert callable(Activity_Data_Nilai.__init__)


def test_activity_data_nilai_constructor_args():
    sig = inspect.signature(Activity_Data_Nilai.__init__)
    params = list(sig.parameters.keys())



def test_activity_data_mahasiswa_is_not_abstract():
    assert not inspect.isabstract(Activity_Data_Mahasiswa)


def test_activity_data_mahasiswa_constructor_exists():
    assert callable(Activity_Data_Mahasiswa.__init__)


def test_activity_data_mahasiswa_constructor_args():
    sig = inspect.signature(Activity_Data_Mahasiswa.__init__)
    params = list(sig.parameters.keys())



def test_view_control_nilai_is_not_abstract():
    assert not inspect.isabstract(view_control_Nilai)


def test_view_control_nilai_constructor_exists():
    assert callable(view_control_Nilai.__init__)


def test_view_control_nilai_constructor_args():
    sig = inspect.signature(view_control_Nilai.__init__)
    params = list(sig.parameters.keys())



def test_view_control_mahasiswa_is_not_abstract():
    assert not inspect.isabstract(view_control_Mahasiswa)


def test_view_control_mahasiswa_constructor_exists():
    assert callable(view_control_Mahasiswa.__init__)


def test_view_control_mahasiswa_constructor_args():
    sig = inspect.signature(view_control_Mahasiswa.__init__)
    params = list(sig.parameters.keys())



def test_dao_nilai_is_not_abstract():
    assert not inspect.isabstract(DAO_Nilai)


def test_dao_nilai_constructor_exists():
    assert callable(DAO_Nilai.__init__)


def test_dao_nilai_constructor_args():
    sig = inspect.signature(DAO_Nilai.__init__)
    params = list(sig.parameters.keys())
    assert "tugas" in params, "Missing parameter 'tugas'"
    assert "uas" in params, "Missing parameter 'uas'"
    assert "uts" in params, "Missing parameter 'uts'"
    assert "namaMk" in params, "Missing parameter 'namaMk'"

def test_dao_nilai_has_tugas():
    assert hasattr(DAO_Nilai, "tugas")
    descriptor = None
    for klass in DAO_Nilai.__mro__:
        if "tugas" in klass.__dict__:
            descriptor = klass.__dict__["tugas"]
            break
    assert isinstance(descriptor, property)

def test_dao_nilai_has_uas():
    assert hasattr(DAO_Nilai, "uas")
    descriptor = None
    for klass in DAO_Nilai.__mro__:
        if "uas" in klass.__dict__:
            descriptor = klass.__dict__["uas"]
            break
    assert isinstance(descriptor, property)

def test_dao_nilai_has_uts():
    assert hasattr(DAO_Nilai, "uts")
    descriptor = None
    for klass in DAO_Nilai.__mro__:
        if "uts" in klass.__dict__:
            descriptor = klass.__dict__["uts"]
            break
    assert isinstance(descriptor, property)

def test_dao_nilai_has_namaMk():
    assert hasattr(DAO_Nilai, "namaMk")
    descriptor = None
    for klass in DAO_Nilai.__mro__:
        if "namaMk" in klass.__dict__:
            descriptor = klass.__dict__["namaMk"]
            break
    assert isinstance(descriptor, property)



def test_dao_mahasiswa_is_not_abstract():
    assert not inspect.isabstract(DAO_Mahasiswa)


def test_dao_mahasiswa_constructor_exists():
    assert callable(DAO_Mahasiswa.__init__)


def test_dao_mahasiswa_constructor_args():
    sig = inspect.signature(DAO_Mahasiswa.__init__)
    params = list(sig.parameters.keys())
    assert "nama" in params, "Missing parameter 'nama'"
    assert "tahun" in params, "Missing parameter 'tahun'"
    assert "nim" in params, "Missing parameter 'nim'"

def test_dao_mahasiswa_has_nama():
    assert hasattr(DAO_Mahasiswa, "nama")
    descriptor = None
    for klass in DAO_Mahasiswa.__mro__:
        if "nama" in klass.__dict__:
            descriptor = klass.__dict__["nama"]
            break
    assert isinstance(descriptor, property)

def test_dao_mahasiswa_has_tahun():
    assert hasattr(DAO_Mahasiswa, "tahun")
    descriptor = None
    for klass in DAO_Mahasiswa.__mro__:
        if "tahun" in klass.__dict__:
            descriptor = klass.__dict__["tahun"]
            break
    assert isinstance(descriptor, property)

def test_dao_mahasiswa_has_nim():
    assert hasattr(DAO_Mahasiswa, "nim")
    descriptor = None
    for klass in DAO_Mahasiswa.__mro__:
        if "nim" in klass.__dict__:
            descriptor = klass.__dict__["nim"]
            break
    assert isinstance(descriptor, property)



def test_aplikasi_input_nilai_matakuliah_component_is_not_abstract():
    assert not inspect.isabstract(Aplikasi_Input_Nilai_Matakuliah_Component)


def test_aplikasi_input_nilai_matakuliah_component_constructor_exists():
    assert callable(Aplikasi_Input_Nilai_Matakuliah_Component.__init__)


def test_aplikasi_input_nilai_matakuliah_component_constructor_args():
    sig = inspect.signature(Aplikasi_Input_Nilai_Matakuliah_Component.__init__)
    params = list(sig.parameters.keys())



def test_dosen_actor_is_not_abstract():
    assert not inspect.isabstract(Dosen_Actor)


def test_dosen_actor_constructor_exists():
    assert callable(Dosen_Actor.__init__)


def test_dosen_actor_constructor_args():
    sig = inspect.signature(Dosen_Actor.__init__)
    params = list(sig.parameters.keys())



def test_nilai_is_not_abstract():
    assert not inspect.isabstract(Nilai)


def test_nilai_constructor_exists():
    assert callable(Nilai.__init__)


def test_nilai_constructor_args():
    sig = inspect.signature(Nilai.__init__)
    params = list(sig.parameters.keys())
    assert "tugas" in params, "Missing parameter 'tugas'"
    assert "uts" in params, "Missing parameter 'uts'"
    assert "uas" in params, "Missing parameter 'uas'"
    assert "namaMK" in params, "Missing parameter 'namaMK'"

def test_nilai_has_tugas():
    assert hasattr(Nilai, "tugas")
    descriptor = None
    for klass in Nilai.__mro__:
        if "tugas" in klass.__dict__:
            descriptor = klass.__dict__["tugas"]
            break
    assert isinstance(descriptor, property)

def test_nilai_has_uts():
    assert hasattr(Nilai, "uts")
    descriptor = None
    for klass in Nilai.__mro__:
        if "uts" in klass.__dict__:
            descriptor = klass.__dict__["uts"]
            break
    assert isinstance(descriptor, property)

def test_nilai_has_uas():
    assert hasattr(Nilai, "uas")
    descriptor = None
    for klass in Nilai.__mro__:
        if "uas" in klass.__dict__:
            descriptor = klass.__dict__["uas"]
            break
    assert isinstance(descriptor, property)

def test_nilai_has_namaMK():
    assert hasattr(Nilai, "namaMK")
    descriptor = None
    for klass in Nilai.__mro__:
        if "namaMK" in klass.__dict__:
            descriptor = klass.__dict__["namaMK"]
            break
    assert isinstance(descriptor, property)



def test_mahasiswa_is_not_abstract():
    assert not inspect.isabstract(Mahasiswa)


def test_mahasiswa_constructor_exists():
    assert callable(Mahasiswa.__init__)


def test_mahasiswa_constructor_args():
    sig = inspect.signature(Mahasiswa.__init__)
    params = list(sig.parameters.keys())
    assert "nama" in params, "Missing parameter 'nama'"
    assert "tahun" in params, "Missing parameter 'tahun'"
    assert "nim" in params, "Missing parameter 'nim'"

def test_mahasiswa_has_nama():
    assert hasattr(Mahasiswa, "nama")
    descriptor = None
    for klass in Mahasiswa.__mro__:
        if "nama" in klass.__dict__:
            descriptor = klass.__dict__["nama"]
            break
    assert isinstance(descriptor, property)

def test_mahasiswa_has_tahun():
    assert hasattr(Mahasiswa, "tahun")
    descriptor = None
    for klass in Mahasiswa.__mro__:
        if "tahun" in klass.__dict__:
            descriptor = klass.__dict__["tahun"]
            break
    assert isinstance(descriptor, property)

def test_mahasiswa_has_nim():
    assert hasattr(Mahasiswa, "nim")
    descriptor = None
    for klass in Mahasiswa.__mro__:
        if "nim" in klass.__dict__:
            descriptor = klass.__dict__["nim"]
            break
    assert isinstance(descriptor, property)


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
Menghapus_Nilai_external_strategy = st.builds(
    Menghapus_Nilai_external,
)
Menghapus_Mahasiswa_external_strategy = st.builds(
    Menghapus_Mahasiswa_external,
)
Mengubah_Data_Nilai_external_strategy = st.builds(
    Mengubah_Data_Nilai_external,
)
Mengubah_Data_Mahasiswa_external_strategy = st.builds(
    Mengubah_Data_Mahasiswa_external,
)
Menambah_Data_Nilai_external_strategy = st.builds(
    Menambah_Data_Nilai_external,
)
Menambah_Data_Mahasiswa_external_strategy = st.builds(
    Menambah_Data_Mahasiswa_external,
)
Melihat_Data_Nilai_external_strategy = st.builds(
    Melihat_Data_Nilai_external,
)
Melihat_Data_Mahasiswa_external_strategy = st.builds(
    Melihat_Data_Mahasiswa_external,
)
Activity_Input_Mahasiswa_strategy = st.builds(
    Activity_Input_Mahasiswa,
)
Activity_Data_Nilai_strategy = st.builds(
    Activity_Data_Nilai,
)
Activity_Data_Mahasiswa_strategy = st.builds(
    Activity_Data_Mahasiswa,
)
view_control_Nilai_strategy = st.builds(
    view_control_Nilai,
)
view_control_Mahasiswa_strategy = st.builds(
    view_control_Mahasiswa,
)
DAO_Nilai_strategy = st.builds(
    DAO_Nilai,
    tugas=
        safe_text,
    uas=
        safe_text,
    uts=
        safe_text,
    namaMk=
        safe_text
)
DAO_Mahasiswa_strategy = st.builds(
    DAO_Mahasiswa,
    nama=
        safe_text,
    tahun=
        safe_text,
    nim=
        safe_text
)
Aplikasi_Input_Nilai_Matakuliah_Component_strategy = st.builds(
    Aplikasi_Input_Nilai_Matakuliah_Component,
)
Dosen_Actor_strategy = st.builds(
    Dosen_Actor,
)
Nilai_strategy = st.builds(
    Nilai,
    tugas=
        st.integers(),
    uts=
        st.integers(),
    uas=
        st.integers(),
    namaMK=
        safe_text
)
Mahasiswa_strategy = st.builds(
    Mahasiswa,
    nama=
        safe_text,
    tahun=
        safe_text,
    nim=
        safe_text
)

@given(instance=Menghapus_Nilai_external_strategy)
@settings(max_examples=50)
def test_menghapus_nilai_external_instantiation(instance):
    assert isinstance(instance, Menghapus_Nilai_external)

@given(instance=Menghapus_Mahasiswa_external_strategy)
@settings(max_examples=50)
def test_menghapus_mahasiswa_external_instantiation(instance):
    assert isinstance(instance, Menghapus_Mahasiswa_external)

@given(instance=Mengubah_Data_Nilai_external_strategy)
@settings(max_examples=50)
def test_mengubah_data_nilai_external_instantiation(instance):
    assert isinstance(instance, Mengubah_Data_Nilai_external)

@given(instance=Mengubah_Data_Mahasiswa_external_strategy)
@settings(max_examples=50)
def test_mengubah_data_mahasiswa_external_instantiation(instance):
    assert isinstance(instance, Mengubah_Data_Mahasiswa_external)

@given(instance=Menambah_Data_Nilai_external_strategy)
@settings(max_examples=50)
def test_menambah_data_nilai_external_instantiation(instance):
    assert isinstance(instance, Menambah_Data_Nilai_external)

@given(instance=Menambah_Data_Mahasiswa_external_strategy)
@settings(max_examples=50)
def test_menambah_data_mahasiswa_external_instantiation(instance):
    assert isinstance(instance, Menambah_Data_Mahasiswa_external)

@given(instance=Melihat_Data_Nilai_external_strategy)
@settings(max_examples=50)
def test_melihat_data_nilai_external_instantiation(instance):
    assert isinstance(instance, Melihat_Data_Nilai_external)

@given(instance=Melihat_Data_Mahasiswa_external_strategy)
@settings(max_examples=50)
def test_melihat_data_mahasiswa_external_instantiation(instance):
    assert isinstance(instance, Melihat_Data_Mahasiswa_external)

@given(instance=Activity_Input_Mahasiswa_strategy)
@settings(max_examples=50)
def test_activity_input_mahasiswa_instantiation(instance):
    assert isinstance(instance, Activity_Input_Mahasiswa)

@given(instance=Activity_Data_Nilai_strategy)
@settings(max_examples=50)
def test_activity_data_nilai_instantiation(instance):
    assert isinstance(instance, Activity_Data_Nilai)

@given(instance=Activity_Data_Mahasiswa_strategy)
@settings(max_examples=50)
def test_activity_data_mahasiswa_instantiation(instance):
    assert isinstance(instance, Activity_Data_Mahasiswa)

@given(instance=view_control_Nilai_strategy)
@settings(max_examples=50)
def test_view_control_nilai_instantiation(instance):
    assert isinstance(instance, view_control_Nilai)

@given(instance=view_control_Mahasiswa_strategy)
@settings(max_examples=50)
def test_view_control_mahasiswa_instantiation(instance):
    assert isinstance(instance, view_control_Mahasiswa)

@given(instance=DAO_Nilai_strategy)
@settings(max_examples=50)
def test_dao_nilai_instantiation(instance):
    assert isinstance(instance, DAO_Nilai)



@given(instance=DAO_Nilai_strategy)
def test_dao_nilai_tugas_setter(instance):
    original = instance.tugas
    instance.tugas = original
    assert instance.tugas == original



@given(instance=DAO_Nilai_strategy)
def test_dao_nilai_uas_setter(instance):
    original = instance.uas
    instance.uas = original
    assert instance.uas == original



@given(instance=DAO_Nilai_strategy)
def test_dao_nilai_uts_setter(instance):
    original = instance.uts
    instance.uts = original
    assert instance.uts == original



@given(instance=DAO_Nilai_strategy)
def test_dao_nilai_namaMk_setter(instance):
    original = instance.namaMk
    instance.namaMk = original
    assert instance.namaMk == original

@given(instance=DAO_Mahasiswa_strategy)
@settings(max_examples=50)
def test_dao_mahasiswa_instantiation(instance):
    assert isinstance(instance, DAO_Mahasiswa)



@given(instance=DAO_Mahasiswa_strategy)
def test_dao_mahasiswa_nama_setter(instance):
    original = instance.nama
    instance.nama = original
    assert instance.nama == original



@given(instance=DAO_Mahasiswa_strategy)
def test_dao_mahasiswa_tahun_setter(instance):
    original = instance.tahun
    instance.tahun = original
    assert instance.tahun == original



@given(instance=DAO_Mahasiswa_strategy)
def test_dao_mahasiswa_nim_setter(instance):
    original = instance.nim
    instance.nim = original
    assert instance.nim == original

@given(instance=Aplikasi_Input_Nilai_Matakuliah_Component_strategy)
@settings(max_examples=50)
def test_aplikasi_input_nilai_matakuliah_component_instantiation(instance):
    assert isinstance(instance, Aplikasi_Input_Nilai_Matakuliah_Component)

@given(instance=Dosen_Actor_strategy)
@settings(max_examples=50)
def test_dosen_actor_instantiation(instance):
    assert isinstance(instance, Dosen_Actor)

@given(instance=Nilai_strategy)
@settings(max_examples=50)
def test_nilai_instantiation(instance):
    assert isinstance(instance, Nilai)



@given(instance=Nilai_strategy)
def test_nilai_tugas_setter(instance):
    original = instance.tugas
    instance.tugas = original
    assert instance.tugas == original



@given(instance=Nilai_strategy)
def test_nilai_uts_setter(instance):
    original = instance.uts
    instance.uts = original
    assert instance.uts == original



@given(instance=Nilai_strategy)
def test_nilai_uas_setter(instance):
    original = instance.uas
    instance.uas = original
    assert instance.uas == original



@given(instance=Nilai_strategy)
def test_nilai_namaMK_setter(instance):
    original = instance.namaMK
    instance.namaMK = original
    assert instance.namaMK == original

@given(instance=Mahasiswa_strategy)
@settings(max_examples=50)
def test_mahasiswa_instantiation(instance):
    assert isinstance(instance, Mahasiswa)



@given(instance=Mahasiswa_strategy)
def test_mahasiswa_nama_setter(instance):
    original = instance.nama
    instance.nama = original
    assert instance.nama == original



@given(instance=Mahasiswa_strategy)
def test_mahasiswa_tahun_setter(instance):
    original = instance.tahun
    instance.tahun = original
    assert instance.tahun == original



@given(instance=Mahasiswa_strategy)
def test_mahasiswa_nim_setter(instance):
    original = instance.nim
    instance.nim = original
    assert instance.nim == original
