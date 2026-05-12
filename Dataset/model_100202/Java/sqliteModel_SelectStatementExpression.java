





import java.util.List;
import java.util.ArrayList;

public class sqliteModel_SelectStatementExpression extends Expression {

    private boolean not_;
    private boolean exists;



    public sqliteModel_SelectStatementExpression(
        boolean not_,        boolean exists    ) {
        super(
        );
        this.not_ = not_;
        this.exists = exists;
    }


    public boolean getNot_() {
        return not_;
    }

    public void setNot_(boolean not_) {
        this.not_ = not_;
    }
    public boolean getExists() {
        return exists;
    }

    public void setExists(boolean exists) {
        this.exists = exists;
    }


}