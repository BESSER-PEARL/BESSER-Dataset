





import java.util.List;
import java.util.ArrayList;

public class problog_ImportLibrary extends Statement {

    private String name;



    public problog_ImportLibrary(
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