





import java.util.List;
import java.util.ArrayList;

public class fuml_Kernel_ElementImport extends Element {

    private String alias;
    private String visibility;



    public fuml_Kernel_ElementImport(
        String alias,        String visibility    ) {
        super(
        );
        this.alias = alias;
        this.visibility = visibility;
    }


    public String getAlias() {
        return alias;
    }

    public void setAlias(String alias) {
        this.alias = alias;
    }
    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }


}