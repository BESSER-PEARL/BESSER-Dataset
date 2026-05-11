





import java.util.List;
import java.util.ArrayList;

public class my_Column extends NamedElement {

    private boolean primary;
    private String type;
    private boolean unique;
    private int size;



    public my_Column(
        boolean primary,        String type,        boolean unique,        int size    ) {
        super(
        );
        this.primary = primary;
        this.type = type;
        this.unique = unique;
        this.size = size;
    }


    public boolean getPrimary() {
        return primary;
    }

    public void setPrimary(boolean primary) {
        this.primary = primary;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public boolean getUnique() {
        return unique;
    }

    public void setUnique(boolean unique) {
        this.unique = unique;
    }
    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }


}