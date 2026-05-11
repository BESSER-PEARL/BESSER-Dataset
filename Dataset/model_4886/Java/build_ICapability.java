





import java.util.List;
import java.util.ArrayList;

public class build_ICapability  {

    private String version;
    private String name;
    private String namespace;





    private build_IBuildUnit build_ibuildunit;


    public build_ICapability(
        String version,        String name,        String namespace    ) {
        this.version = version;
        this.name = name;
        this.namespace = namespace;
    }


    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getNamespace() {
        return namespace;
    }

    public void setNamespace(String namespace) {
        this.namespace = namespace;
    }

    public build_IBuildUnit getBuild_ibuildunit() {
        return build_ibuildunit;
    }

    public void setBuild_ibuildunit(build_IBuildUnit build_ibuildunit) {
        this.build_ibuildunit = build_ibuildunit;
    }

}