





import java.util.List;
import java.util.ArrayList;

public class JPA_OneToOne extends Anotation {

    private String referencedColumnName;
    private boolean updatable;
    private String name;



    public JPA_OneToOne(
        String referencedColumnName,        boolean updatable,        String name    ) {
        super(
        );
        this.referencedColumnName = referencedColumnName;
        this.updatable = updatable;
        this.name = name;
    }


    public String getReferencedcolumnname() {
        return referencedColumnName;
    }

    public void setReferencedcolumnname(String referencedColumnName) {
        this.referencedColumnName = referencedColumnName;
    }
    public boolean getUpdatable() {
        return updatable;
    }

    public void setUpdatable(boolean updatable) {
        this.updatable = updatable;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}