





import java.util.List;
import java.util.ArrayList;

public class UML2_UseCase extends BehavioredClassifier {






    private List<UML2_Extend> uml2_extends;




    private UML2_Include uml2_include;




    private List<UML2_Include> uml2_includes;




    private UML2_Extend uml2_extend;




    private UML2_Include uml2_include;




    private UML2_Extend uml2_extend;


    public UML2_UseCase(
    ) {
        super(
        );
        this.uml2_extends = new ArrayList<>();
        this.uml2_includes = new ArrayList<>();
    }

    public UML2_UseCase(
        ArrayList<UML2_Extend> uml2_extends,        ArrayList<UML2_Include> uml2_includes    ) {
        this.uml2_extends = uml2_extends;
        this.uml2_includes = uml2_includes;
    }


    public List<UML2_Extend> getUml2_extends() {
        return uml2_extends;
    }

    public void addUml2_extend(Uml2_extend uml2_extend) {
        this.uml2_extends.add(uml2_extend);
    }
    public UML2_Include getUml2_include() {
        return uml2_include;
    }

    public void setUml2_include(UML2_Include uml2_include) {
        this.uml2_include = uml2_include;
    }
    public List<UML2_Include> getUml2_includes() {
        return uml2_includes;
    }

    public void addUml2_include(Uml2_include uml2_include) {
        this.uml2_includes.add(uml2_include);
    }
    public UML2_Extend getUml2_extend() {
        return uml2_extend;
    }

    public void setUml2_extend(UML2_Extend uml2_extend) {
        this.uml2_extend = uml2_extend;
    }
    public UML2_Include getUml2_include() {
        return uml2_include;
    }

    public void setUml2_include(UML2_Include uml2_include) {
        this.uml2_include = uml2_include;
    }
    public UML2_Extend getUml2_extend() {
        return uml2_extend;
    }

    public void setUml2_extend(UML2_Extend uml2_extend) {
        this.uml2_extend = uml2_extend;
    }

}