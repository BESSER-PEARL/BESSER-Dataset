





import java.util.List;
import java.util.ArrayList;

public class pgohttpestest_A  {

    private String name;
    private int value;





    private pgohttpestest_Root pgohttpestest_root;


    public pgohttpestest_A(
        String name,        int value    ) {
        this.name = name;
        this.value = value;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }

    public pgohttpestest_Root getPgohttpestest_root() {
        return pgohttpestest_root;
    }

    public void setPgohttpestest_root(pgohttpestest_Root pgohttpestest_root) {
        this.pgohttpestest_root = pgohttpestest_root;
    }

}