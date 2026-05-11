





import java.util.List;
import java.util.ArrayList;

public class dft_Parametrized extends GalileoNodeType {

    private String typeName;
    private String parameter;



    public dft_Parametrized(
        String typeName,        String parameter    ) {
        super(
        );
        this.typeName = typeName;
        this.parameter = parameter;
    }


    public String getTypename() {
        return typeName;
    }

    public void setTypename(String typeName) {
        this.typeName = typeName;
    }
    public String getParameter() {
        return parameter;
    }

    public void setParameter(String parameter) {
        this.parameter = parameter;
    }


}