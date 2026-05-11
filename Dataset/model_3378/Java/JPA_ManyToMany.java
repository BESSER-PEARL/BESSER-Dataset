





import java.util.List;
import java.util.ArrayList;

public class JPA_ManyToMany extends Anotation {

    private String name;
    private String inverseJoinColumn;
    private String joinColumn;



    public JPA_ManyToMany(
        String name,        String inverseJoinColumn,        String joinColumn    ) {
        super(
        );
        this.name = name;
        this.inverseJoinColumn = inverseJoinColumn;
        this.joinColumn = joinColumn;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getInversejoincolumn() {
        return inverseJoinColumn;
    }

    public void setInversejoincolumn(String inverseJoinColumn) {
        this.inverseJoinColumn = inverseJoinColumn;
    }
    public String getJoincolumn() {
        return joinColumn;
    }

    public void setJoincolumn(String joinColumn) {
        this.joinColumn = joinColumn;
    }


}