





import java.util.List;
import java.util.ArrayList;

public class adb_TypeDeclaration extends BasicDeclaration {

    private String name;



    public adb_TypeDeclaration(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}