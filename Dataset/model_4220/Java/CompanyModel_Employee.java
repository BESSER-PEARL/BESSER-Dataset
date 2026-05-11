





import java.util.List;
import java.util.ArrayList;

public class CompanyModel_Employee  {

    private boolean isManager;
    private String name;





    private CompanyModel_Department companymodel_department;


    public CompanyModel_Employee(
        boolean isManager,        String name    ) {
        this.isManager = isManager;
        this.name = name;
    }


    public boolean getIsmanager() {
        return isManager;
    }

    public void setIsmanager(boolean isManager) {
        this.isManager = isManager;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public CompanyModel_Department getCompanymodel_department() {
        return companymodel_department;
    }

    public void setCompanymodel_department(CompanyModel_Department companymodel_department) {
        this.companymodel_department = companymodel_department;
    }

}