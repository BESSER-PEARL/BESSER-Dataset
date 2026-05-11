





import java.util.List;
import java.util.ArrayList;

public class article_JavaElement extends LinkTarget {

    private String classFile;



    public article_JavaElement(
        String classFile    ) {
        super(
        );
        this.classFile = classFile;
    }


    public String getClassfile() {
        return classFile;
    }

    public void setClassfile(String classFile) {
        this.classFile = classFile;
    }


}