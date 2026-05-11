





import java.util.List;
import java.util.ArrayList;

public class SQL2003_V3_Column extends StructuralComponent {

    private String default;



    public SQL2003_V3_Column(
        String default    ) {
        super(
        );
        this.default = default;
    }


    public String getDefault() {
        return default;
    }

    public void setDefault(String default) {
        this.default = default;
    }


}