





import java.util.List;
import java.util.ArrayList;

public class company104_Goal extends Interval {

    private String statement;





    private company104_Company company104_company;


    public company104_Goal(
        String statement    ) {
        super(
        );
        this.statement = statement;
    }


    public String getStatement() {
        return statement;
    }

    public void setStatement(String statement) {
        this.statement = statement;
    }

    public company104_Company getCompany104_company() {
        return company104_company;
    }

    public void setCompany104_company(company104_Company company104_company) {
        this.company104_company = company104_company;
    }

}