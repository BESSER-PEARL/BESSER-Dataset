





import java.util.List;
import java.util.ArrayList;

public class flat11_TemplateType  {

    private String declaration;





    private List<flat11_TransitionType> flat11_transitiontypes;




    private flat11_ParameterType flat11_parametertype;




    private flat11_NameType flat11_nametype;




    private flat11_InitType flat11_inittype;




    private flat11_NtaType flat11_ntatype;




    private List<flat11_LocationType> flat11_locationtypes;




    private flat11_DocumentRoot flat11_documentroot;


    public flat11_TemplateType(
        String declaration    ) {
        this.declaration = declaration;
        this.flat11_transitiontypes = new ArrayList<>();
        this.flat11_locationtypes = new ArrayList<>();
    }

    public flat11_TemplateType(
        String declaration        ArrayList<flat11_TransitionType> flat11_transitiontypes,        ArrayList<flat11_LocationType> flat11_locationtypes    ) {
        this.declaration = declaration;
        this.flat11_transitiontypes = flat11_transitiontypes;
        this.flat11_locationtypes = flat11_locationtypes;
    }

    public String getDeclaration() {
        return declaration;
    }

    public void setDeclaration(String declaration) {
        this.declaration = declaration;
    }

    public List<flat11_TransitionType> getFlat11_transitiontypes() {
        return flat11_transitiontypes;
    }

    public void addFlat11_transitiontype(Flat11_transitiontype flat11_transitiontype) {
        this.flat11_transitiontypes.add(flat11_transitiontype);
    }
    public flat11_ParameterType getFlat11_parametertype() {
        return flat11_parametertype;
    }

    public void setFlat11_parametertype(flat11_ParameterType flat11_parametertype) {
        this.flat11_parametertype = flat11_parametertype;
    }
    public flat11_NameType getFlat11_nametype() {
        return flat11_nametype;
    }

    public void setFlat11_nametype(flat11_NameType flat11_nametype) {
        this.flat11_nametype = flat11_nametype;
    }
    public flat11_InitType getFlat11_inittype() {
        return flat11_inittype;
    }

    public void setFlat11_inittype(flat11_InitType flat11_inittype) {
        this.flat11_inittype = flat11_inittype;
    }
    public flat11_NtaType getFlat11_ntatype() {
        return flat11_ntatype;
    }

    public void setFlat11_ntatype(flat11_NtaType flat11_ntatype) {
        this.flat11_ntatype = flat11_ntatype;
    }
    public List<flat11_LocationType> getFlat11_locationtypes() {
        return flat11_locationtypes;
    }

    public void addFlat11_locationtype(Flat11_locationtype flat11_locationtype) {
        this.flat11_locationtypes.add(flat11_locationtype);
    }
    public flat11_DocumentRoot getFlat11_documentroot() {
        return flat11_documentroot;
    }

    public void setFlat11_documentroot(flat11_DocumentRoot flat11_documentroot) {
        this.flat11_documentroot = flat11_documentroot;
    }

}