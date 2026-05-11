





import java.util.List;
import java.util.ArrayList;

public class core_RequireDeclaration extends RepresentModel {

    private String name;
    private String default;



    public core_RequireDeclaration(
        String name,        String default    ) {
        super(
        );
        this.name = name;
        this.default = default;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDefault() {
        return default;
    }

    public void setDefault(String default) {
        this.default = default;
    }


}