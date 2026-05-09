





import java.util.List;
import java.util.ArrayList;

public class myDsl_MultipleFile  {

    private String name;





    private myDsl_Directories mydsl_directories;


    public myDsl_MultipleFile(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public myDsl_Directories getMydsl_directories() {
        return mydsl_directories;
    }

    public void setMydsl_directories(myDsl_Directories mydsl_directories) {
        this.mydsl_directories = mydsl_directories;
    }

}