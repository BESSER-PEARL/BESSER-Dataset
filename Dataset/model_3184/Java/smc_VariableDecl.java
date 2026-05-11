





import java.util.List;
import java.util.ArrayList;

public class smc_VariableDecl extends Command {

    private String type;
    private boolean array;
    private String visibility;
    private int length;
    private String name;



    public smc_VariableDecl(
        String type,        boolean array,        String visibility,        int length,        String name    ) {
        super(
        );
        this.type = type;
        this.array = array;
        this.visibility = visibility;
        this.length = length;
        this.name = name;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public boolean getArray() {
        return array;
    }

    public void setArray(boolean array) {
        this.array = array;
    }
    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }
    public int getLength() {
        return length;
    }

    public void setLength(int length) {
        this.length = length;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}