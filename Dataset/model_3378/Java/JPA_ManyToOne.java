





import java.util.List;
import java.util.ArrayList;

public class JPA_ManyToOne extends Anotation {

    private String joinColumn;
    private boolean nullable;
    private String fetch;



    public JPA_ManyToOne(
        String joinColumn,        boolean nullable,        String fetch    ) {
        super(
        );
        this.joinColumn = joinColumn;
        this.nullable = nullable;
        this.fetch = fetch;
    }


    public String getJoincolumn() {
        return joinColumn;
    }

    public void setJoincolumn(String joinColumn) {
        this.joinColumn = joinColumn;
    }
    public boolean getNullable() {
        return nullable;
    }

    public void setNullable(boolean nullable) {
        this.nullable = nullable;
    }
    public String getFetch() {
        return fetch;
    }

    public void setFetch(String fetch) {
        this.fetch = fetch;
    }


}