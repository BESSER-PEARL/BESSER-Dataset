





import java.util.List;
import java.util.ArrayList;

public class JPA_OneToOne extends Anotation {

    private String referencedColumnName;
    private String name;
    private boolean updatable;



    public JPA_OneToOne(
        String referencedColumnName,        String name,        boolean updatable    ) {
        super(
        );
        this.referencedColumnName = referencedColumnName;
        this.name = name;
        this.updatable = updatable;
    }


    public String getReferencedcolumnname() {
        return referencedColumnName;
    }

    public void setReferencedcolumnname(String referencedColumnName) {
        this.referencedColumnName = referencedColumnName;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getUpdatable() {
        return updatable;
    }

    public void setUpdatable(boolean updatable) {
        this.updatable = updatable;
    }


}