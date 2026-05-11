





import java.util.List;
import java.util.ArrayList;

public class xpdl2_ExternalPackage extends Extensible {

    private String name;
    private String id;
    private String href;





    private xpdl2_ExternalPackages xpdl2_externalpackages;


    public xpdl2_ExternalPackage(
        String name,        String id,        String href    ) {
        super(
        );
        this.name = name;
        this.id = id;
        this.href = href;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
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

    public xpdl2_ExternalPackages getXpdl2_externalpackages() {
        return xpdl2_externalpackages;
    }

    public void setXpdl2_externalpackages(xpdl2_ExternalPackages xpdl2_externalpackages) {
        this.xpdl2_externalpackages = xpdl2_externalpackages;
    }

}