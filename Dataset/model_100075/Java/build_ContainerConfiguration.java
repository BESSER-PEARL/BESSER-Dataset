





import java.util.List;
import java.util.ArrayList;

public class build_ContainerConfiguration  {

    private String name;
    private String documentation;





    private build_IType build_itype;




    private build_BuildUnit build_buildunit;


    public build_ContainerConfiguration(
        String name,        String documentation    ) {
        this.name = name;
        this.documentation = documentation;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDocumentation() {
        return documentation;
    }

    public void setDocumentation(String documentation) {
        this.documentation = documentation;
    }

    public build_IType getBuild_itype() {
        return build_itype;
    }

    public void setBuild_itype(build_IType build_itype) {
        this.build_itype = build_itype;
    }
    public build_BuildUnit getBuild_buildunit() {
        return build_buildunit;
    }

    public void setBuild_buildunit(build_BuildUnit build_buildunit) {
        this.build_buildunit = build_buildunit;
    }

}