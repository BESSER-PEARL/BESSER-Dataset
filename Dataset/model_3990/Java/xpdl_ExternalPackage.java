





import java.util.List;
import java.util.ArrayList;

public class xpdl_ExternalPackage extends Extensible {

    private String id;
    private String href;
    private String name;





    private xpdl_ExternalPackages xpdl_externalpackages;


    public xpdl_ExternalPackage(
        String id,        String href,        String name    ) {
        super(
        );
        this.id = id;
        this.href = href;
        this.name = name;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getHref() {
        return href;
    }

    public void setHref(String href) {
        this.href = href;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public xpdl_ExternalPackages getXpdl_externalpackages() {
        return xpdl_externalpackages;
    }

    public void setXpdl_externalpackages(xpdl_ExternalPackages xpdl_externalpackages) {
        this.xpdl_externalpackages = xpdl_externalpackages;
    }

}