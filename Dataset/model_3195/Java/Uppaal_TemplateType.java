





import java.util.List;
import java.util.ArrayList;

public class Uppaal_TemplateType  {






    private Uppaal_DocumentRoot uppaal_documentroot;




    private Uppaal_NameType uppaal_nametype;




    private List<Uppaal_LocationType> uppaal_locationtypes;




    private List<Uppaal_TransitionType> uppaal_transitiontypes;




    private Uppaal_DeclarationType uppaal_declarationtype;




    private Uppaal_ParameterType uppaal_parametertype;




    private Uppaal_InitType uppaal_inittype;




    private Uppaal_NtaType uppaal_ntatype;


    public Uppaal_TemplateType(
    ) {
        this.uppaal_locationtypes = new ArrayList<>();
        this.uppaal_transitiontypes = new ArrayList<>();
    }

    public Uppaal_TemplateType(
        ArrayList<Uppaal_LocationType> uppaal_locationtypes,        ArrayList<Uppaal_TransitionType> uppaal_transitiontypes    ) {
        this.uppaal_locationtypes = uppaal_locationtypes;
        this.uppaal_transitiontypes = uppaal_transitiontypes;
    }


    public Uppaal_DocumentRoot getUppaal_documentroot() {
        return uppaal_documentroot;
    }

    public void setUppaal_documentroot(Uppaal_DocumentRoot uppaal_documentroot) {
        this.uppaal_documentroot = uppaal_documentroot;
    }
    public Uppaal_NameType getUppaal_nametype() {
        return uppaal_nametype;
    }

    public void setUppaal_nametype(Uppaal_NameType uppaal_nametype) {
        this.uppaal_nametype = uppaal_nametype;
    }
    public List<Uppaal_LocationType> getUppaal_locationtypes() {
        return uppaal_locationtypes;
    }

    public void addUppaal_locationtype(Uppaal_locationtype uppaal_locationtype) {
        this.uppaal_locationtypes.add(uppaal_locationtype);
    }
    public List<Uppaal_TransitionType> getUppaal_transitiontypes() {
        return uppaal_transitiontypes;
    }

    public void addUppaal_transitiontype(Uppaal_transitiontype uppaal_transitiontype) {
        this.uppaal_transitiontypes.add(uppaal_transitiontype);
    }
    public Uppaal_DeclarationType getUppaal_declarationtype() {
        return uppaal_declarationtype;
    }

    public void setUppaal_declarationtype(Uppaal_DeclarationType uppaal_declarationtype) {
        this.uppaal_declarationtype = uppaal_declarationtype;
    }
    public Uppaal_ParameterType getUppaal_parametertype() {
        return uppaal_parametertype;
    }

    public void setUppaal_parametertype(Uppaal_ParameterType uppaal_parametertype) {
        this.uppaal_parametertype = uppaal_parametertype;
    }
    public Uppaal_InitType getUppaal_inittype() {
        return uppaal_inittype;
    }

    public void setUppaal_inittype(Uppaal_InitType uppaal_inittype) {
        this.uppaal_inittype = uppaal_inittype;
    }
    public Uppaal_NtaType getUppaal_ntatype() {
        return uppaal_ntatype;
    }

    public void setUppaal_ntatype(Uppaal_NtaType uppaal_ntatype) {
        this.uppaal_ntatype = uppaal_ntatype;
    }

}