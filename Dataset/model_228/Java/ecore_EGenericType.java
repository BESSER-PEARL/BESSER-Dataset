





import java.util.List;
import java.util.ArrayList;

public class ecore_EGenericType  {






    private ecore_EClass ecore_eclass;




    private List<ecore_EGenericType> ecore_egenerictypes;




    private ecore_EGenericType ecore_egenerictype;




    private ecore_EOperation ecore_eoperation;




    private ecore_EGenericType ecore_egenerictype;




    private ecore_ETypeParameter ecore_etypeparameter;




    private ecore_ETypeParameter ecore_etypeparameter;




    private ecore_EClass ecore_eclass;


    public ecore_EGenericType(
    ) {
        this.ecore_egenerictypes = new ArrayList<>();
    }

    public ecore_EGenericType(
        ArrayList<ecore_EGenericType> ecore_egenerictypes    ) {
        this.ecore_egenerictypes = ecore_egenerictypes;
    }


    public ecore_EClass getEcore_eclass() {
        return ecore_eclass;
    }

    public void setEcore_eclass(ecore_EClass ecore_eclass) {
        this.ecore_eclass = ecore_eclass;
    }
    public List<ecore_EGenericType> getEcore_egenerictypes() {
        return ecore_egenerictypes;
    }

    public void addEcore_egenerictype(Ecore_egenerictype ecore_egenerictype) {
        this.ecore_egenerictypes.add(ecore_egenerictype);
    }
    public ecore_EGenericType getEcore_egenerictype() {
        return ecore_egenerictype;
    }

    public void setEcore_egenerictype(ecore_EGenericType ecore_egenerictype) {
        this.ecore_egenerictype = ecore_egenerictype;
    }
    public ecore_EOperation getEcore_eoperation() {
        return ecore_eoperation;
    }

    public void setEcore_eoperation(ecore_EOperation ecore_eoperation) {
        this.ecore_eoperation = ecore_eoperation;
    }
    public ecore_EGenericType getEcore_egenerictype() {
        return ecore_egenerictype;
    }

    public void setEcore_egenerictype(ecore_EGenericType ecore_egenerictype) {
        this.ecore_egenerictype = ecore_egenerictype;
    }
    public ecore_ETypeParameter getEcore_etypeparameter() {
        return ecore_etypeparameter;
    }

    public void setEcore_etypeparameter(ecore_ETypeParameter ecore_etypeparameter) {
        this.ecore_etypeparameter = ecore_etypeparameter;
    }
    public ecore_ETypeParameter getEcore_etypeparameter() {
        return ecore_etypeparameter;
    }

    public void setEcore_etypeparameter(ecore_ETypeParameter ecore_etypeparameter) {
        this.ecore_etypeparameter = ecore_etypeparameter;
    }
    public ecore_EClass getEcore_eclass() {
        return ecore_eclass;
    }

    public void setEcore_eclass(ecore_EClass ecore_eclass) {
        this.ecore_eclass = ecore_eclass;
    }

}