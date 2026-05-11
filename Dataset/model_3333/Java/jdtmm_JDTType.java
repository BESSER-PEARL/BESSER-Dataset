





import java.util.List;
import java.util.ArrayList;

public class jdtmm_JDTType extends JDTMember {

    private String enum;
    private String interface;
    private String class_;
    private String static;
    private String superClassName;
    private String abstract;
    private String superInterfaceNames;
    private String final;





    private jdtmm_JDTMethod jdtmm_jdtmethod;




    private jdtmm_JDTType jdtmm_jdttype;




    private List<jdtmm_JDTField> jdtmm_jdtfields;




    private List<jdtmm_JDTType> jdtmm_jdttypes;




    private jdtmm_JDTType jdtmm_jdttype;




    private jdtmm_JDTField jdtmm_jdtfield;




    private List<jdtmm_JDTMethod> jdtmm_jdtmethods;




    private jdtmm_JDTType jdtmm_jdttype;




    private jdtmm_JDTField jdtmm_jdtfield;




    private jdtmm_JDTParameter jdtmm_jdtparameter;




    private jdtmm_JDTMethod jdtmm_jdtmethod;


    public jdtmm_JDTType(
        String enum,        String interface,        String class_,        String static,        String superClassName,        String abstract,        String superInterfaceNames,        String final    ) {
        super(
        );
        this.enum = enum;
        this.interface = interface;
        this.class_ = class_;
        this.static = static;
        this.superClassName = superClassName;
        this.abstract = abstract;
        this.superInterfaceNames = superInterfaceNames;
        this.final = final;
        this.jdtmm_jdtfields = new ArrayList<>();
        this.jdtmm_jdttypes = new ArrayList<>();
        this.jdtmm_jdtmethods = new ArrayList<>();
    }

    public jdtmm_JDTType(
        String enum,        String interface,        String class_,        String static,        String superClassName,        String abstract,        String superInterfaceNames,        String final        ArrayList<jdtmm_JDTField> jdtmm_jdtfields,        ArrayList<jdtmm_JDTType> jdtmm_jdttypes,        ArrayList<jdtmm_JDTMethod> jdtmm_jdtmethods    ) {
        this.enum = enum;
        this.interface = interface;
        this.class_ = class_;
        this.static = static;
        this.superClassName = superClassName;
        this.abstract = abstract;
        this.superInterfaceNames = superInterfaceNames;
        this.final = final;
        this.jdtmm_jdtfields = jdtmm_jdtfields;
        this.jdtmm_jdttypes = jdtmm_jdttypes;
        this.jdtmm_jdtmethods = jdtmm_jdtmethods;
    }

    public String getEnum() {
        return enum;
    }

    public void setEnum(String enum) {
        this.enum = enum;
    }
    public String getInterface() {
        return interface;
    }

    public void setInterface(String interface) {
        this.interface = interface;
    }
    public String getClass_() {
        return class_;
    }

    public void setClass_(String class_) {
        this.class_ = class_;
    }
    public String getStatic() {
        return static;
    }

    public void setStatic(String static) {
        this.static = static;
    }
    public String getSuperclassname() {
        return superClassName;
    }

    public void setSuperclassname(String superClassName) {
        this.superClassName = superClassName;
    }
    public String getAbstract() {
        return abstract;
    }

    public void setAbstract(String abstract) {
        this.abstract = abstract;
    }
    public String getSuperinterfacenames() {
        return superInterfaceNames;
    }

    public void setSuperinterfacenames(String superInterfaceNames) {
        this.superInterfaceNames = superInterfaceNames;
    }
    public String getFinal() {
        return final;
    }

    public void setFinal(String final) {
        this.final = final;
    }

    public jdtmm_JDTMethod getJdtmm_jdtmethod() {
        return jdtmm_jdtmethod;
    }

    public void setJdtmm_jdtmethod(jdtmm_JDTMethod jdtmm_jdtmethod) {
        this.jdtmm_jdtmethod = jdtmm_jdtmethod;
    }
    public jdtmm_JDTType getJdtmm_jdttype() {
        return jdtmm_jdttype;
    }

    public void setJdtmm_jdttype(jdtmm_JDTType jdtmm_jdttype) {
        this.jdtmm_jdttype = jdtmm_jdttype;
    }
    public List<jdtmm_JDTField> getJdtmm_jdtfields() {
        return jdtmm_jdtfields;
    }

    public void addJdtmm_jdtfield(Jdtmm_jdtfield jdtmm_jdtfield) {
        this.jdtmm_jdtfields.add(jdtmm_jdtfield);
    }
    public List<jdtmm_JDTType> getJdtmm_jdttypes() {
        return jdtmm_jdttypes;
    }

    public void addJdtmm_jdttype(Jdtmm_jdttype jdtmm_jdttype) {
        this.jdtmm_jdttypes.add(jdtmm_jdttype);
    }
    public jdtmm_JDTType getJdtmm_jdttype() {
        return jdtmm_jdttype;
    }

    public void setJdtmm_jdttype(jdtmm_JDTType jdtmm_jdttype) {
        this.jdtmm_jdttype = jdtmm_jdttype;
    }
    public jdtmm_JDTField getJdtmm_jdtfield() {
        return jdtmm_jdtfield;
    }

    public void setJdtmm_jdtfield(jdtmm_JDTField jdtmm_jdtfield) {
        this.jdtmm_jdtfield = jdtmm_jdtfield;
    }
    public List<jdtmm_JDTMethod> getJdtmm_jdtmethods() {
        return jdtmm_jdtmethods;
    }

    public void addJdtmm_jdtmethod(Jdtmm_jdtmethod jdtmm_jdtmethod) {
        this.jdtmm_jdtmethods.add(jdtmm_jdtmethod);
    }
    public jdtmm_JDTType getJdtmm_jdttype() {
        return jdtmm_jdttype;
    }

    public void setJdtmm_jdttype(jdtmm_JDTType jdtmm_jdttype) {
        this.jdtmm_jdttype = jdtmm_jdttype;
    }
    public jdtmm_JDTField getJdtmm_jdtfield() {
        return jdtmm_jdtfield;
    }

    public void setJdtmm_jdtfield(jdtmm_JDTField jdtmm_jdtfield) {
        this.jdtmm_jdtfield = jdtmm_jdtfield;
    }
    public jdtmm_JDTParameter getJdtmm_jdtparameter() {
        return jdtmm_jdtparameter;
    }

    public void setJdtmm_jdtparameter(jdtmm_JDTParameter jdtmm_jdtparameter) {
        this.jdtmm_jdtparameter = jdtmm_jdtparameter;
    }
    public jdtmm_JDTMethod getJdtmm_jdtmethod() {
        return jdtmm_jdtmethod;
    }

    public void setJdtmm_jdtmethod(jdtmm_JDTMethod jdtmm_jdtmethod) {
        this.jdtmm_jdtmethod = jdtmm_jdtmethod;
    }

}