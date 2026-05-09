





import java.util.List;
import java.util.ArrayList;

public class basic_Alias extends TypeItem {

    private String name;
    private String rawName;





    private basic_File basic_file;


    public basic_Alias(
        String name,        String rawName    ) {
        super(
        );
        this.name = name;
        this.rawName = rawName;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getRawname() {
        return rawName;
    }

    public void setRawname(String rawName) {
        this.rawName = rawName;
    }

    public basic_File getBasic_file() {
        return basic_file;
    }

    public void setBasic_file(basic_File basic_file) {
        this.basic_file = basic_file;
    }

}