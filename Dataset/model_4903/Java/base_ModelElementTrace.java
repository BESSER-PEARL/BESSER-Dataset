





import java.util.List;
import java.util.ArrayList;

public class base_ModelElementTrace extends IdElement {

    private String uri;





    private base_ElementAccess base_elementaccess;


    public base_ModelElementTrace(
        String uri    ) {
        super(
        );
        this.uri = uri;
    }


    public String getUri() {
        return uri;
    }

    public void setUri(String uri) {
        this.uri = uri;
    }

    public base_ElementAccess getBase_elementaccess() {
        return base_elementaccess;
    }

    public void setBase_elementaccess(base_ElementAccess base_elementaccess) {
        this.base_elementaccess = base_elementaccess;
    }

}