





import java.util.List;
import java.util.ArrayList;

public class company104_Agency extends Function {

    private String Status;
    private String Accronym;





    private company104_Company company104_company;


    public company104_Agency(
        String Status,        String Accronym    ) {
        super(
        );
        this.Status = Status;
        this.Accronym = Accronym;
    }


    public String getStatus() {
        return Status;
    }

    public void setStatus(String Status) {
        this.Status = Status;
    }
    public String getAccronym() {
        return Accronym;
    }

    public void setAccronym(String Accronym) {
        this.Accronym = Accronym;
    }

    public company104_Company getCompany104_company() {
        return company104_company;
    }

    public void setCompany104_company(company104_Company company104_company) {
        this.company104_company = company104_company;
    }

}