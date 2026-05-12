





import java.util.List;
import java.util.ArrayList;

public class Class_Diagram_for_Proposed_system_Salary  {

    private String empId;
    private String id;
    private String basicPay;
    private String advances;
    private String EPF;
    private String overtimes;
    private String payDate;
    private String allowances;
    private String ETF;
    private String deductions;



    public Class_Diagram_for_Proposed_system_Salary(
        String empId,        String id,        String basicPay,        String advances,        String EPF,        String overtimes,        String payDate,        String allowances,        String ETF,        String deductions    ) {
        this.empId = empId;
        this.id = id;
        this.basicPay = basicPay;
        this.advances = advances;
        this.EPF = EPF;
        this.overtimes = overtimes;
        this.payDate = payDate;
        this.allowances = allowances;
        this.ETF = ETF;
        this.deductions = deductions;
    }


    public String getEmpid() {
        return empId;
    }

    public void setEmpid(String empId) {
        this.empId = empId;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getBasicpay() {
        return basicPay;
    }

    public void setBasicpay(String basicPay) {
        this.basicPay = basicPay;
    }
    public String getAdvances() {
        return advances;
    }

    public void setAdvances(String advances) {
        this.advances = advances;
    }
    public String getEpf() {
        return EPF;
    }

    public void setEpf(String EPF) {
        this.EPF = EPF;
    }
    public String getOvertimes() {
        return overtimes;
    }

    public void setOvertimes(String overtimes) {
        this.overtimes = overtimes;
    }
    public String getPaydate() {
        return payDate;
    }

    public void setPaydate(String payDate) {
        this.payDate = payDate;
    }
    public String getAllowances() {
        return allowances;
    }

    public void setAllowances(String allowances) {
        this.allowances = allowances;
    }
    public String getEtf() {
        return ETF;
    }

    public void setEtf(String ETF) {
        this.ETF = ETF;
    }
    public String getDeductions() {
        return deductions;
    }

    public void setDeductions(String deductions) {
        this.deductions = deductions;
    }


}