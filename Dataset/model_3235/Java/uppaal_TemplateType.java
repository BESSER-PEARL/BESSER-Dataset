





import java.util.List;
import java.util.ArrayList;

public class uppaal_TemplateType  {

    private String declaration;





    private uppaal_InitType uppaal_inittype;




    private uppaal_NameType uppaal_nametype;




    private List<uppaal_LocationType> uppaal_locationtypes;




    private uppaal_ParameterType uppaal_parametertype;




    private uppaal_DocumentRoot uppaal_documentroot;




    private uppaal_NtaType uppaal_ntatype;


    public uppaal_TemplateType(
        String declaration    ) {
        this.declaration = declaration;
        this.uppaal_locationtypes = new ArrayList<>();
    }

    public uppaal_TemplateType(
        String declaration        ArrayList<uppaal_LocationType> uppaal_locationtypes    ) {
        this.declaration = declaration;
        this.uppaal_locationtypes = uppaal_locationtypes;
    }

    public String getDeclaration() {
        return declaration;
    }

    public void setDeclaration(String declaration) {
        this.declaration = declaration;
    }

    public uppaal_InitType getUppaal_inittype() {
        return uppaal_inittype;
    }

    public void setUppaal_inittype(uppaal_InitType uppaal_inittype) {
        this.uppaal_inittype = uppaal_inittype;
    }
    public uppaal_NameType getUppaal_nametype() {
        return uppaal_nametype;
    }

    public void setUppaal_nametype(uppaal_NameType uppaal_nametype) {
        this.uppaal_nametype = uppaal_nametype;
    }
    public List<uppaal_LocationType> getUppaal_locationtypes() {
        return uppaal_locationtypes;
    }

    public void addUppaal_locationtype(Uppaal_locationtype uppaal_locationtype) {
        this.uppaal_locationtypes.add(uppaal_locationtype);
    }
    public uppaal_ParameterType getUppaal_parametertype() {
        return uppaal_parametertype;
    }

    public void setUppaal_parametertype(uppaal_ParameterType uppaal_parametertype) {
        this.uppaal_parametertype = uppaal_parametertype;
    }
    public uppaal_DocumentRoot getUppaal_documentroot() {
        return uppaal_documentroot;
    }

    public void setUppaal_documentroot(uppaal_DocumentRoot uppaal_documentroot) {
        this.uppaal_documentroot = uppaal_documentroot;
    }
    public uppaal_NtaType getUppaal_ntatype() {
        return uppaal_ntatype;
    }

    public void setUppaal_ntatype(uppaal_NtaType uppaal_ntatype) {
        this.uppaal_ntatype = uppaal_ntatype;
    }

}