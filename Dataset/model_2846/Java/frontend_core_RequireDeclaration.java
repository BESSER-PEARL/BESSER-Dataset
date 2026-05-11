





import java.util.List;
import java.util.ArrayList;

public class frontend_core_RequireDeclaration extends RepresentModel {

    private String default;
    private String name;



    public frontend_core_RequireDeclaration(
        String default,        String name    ) {
        super(
        );
        this.default = default;
        this.name = name;
    }


    public String getDefault() {
        return default;
    }

    public void setDefault(String default) {
        this.default = default;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}