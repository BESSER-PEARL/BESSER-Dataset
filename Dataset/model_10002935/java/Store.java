





import java.util.List;
import java.util.ArrayList;

public class Store  {

    private String SName;
    private int Sid;





    private Product product;




    private member member;




    private Employee employee;


    public Store(
        String SName,        int Sid    ) {
        this.SName = SName;
        this.Sid = Sid;
    }


    public String getSname() {
        return SName;
    }

    public void setSname(String SName) {
        this.SName = SName;
    }
    public int getSid() {
        return Sid;
    }

    public void setSid(int Sid) {
        this.Sid = Sid;
    }

    public Product getProduct() {
        return product;
    }

    public void setProduct(Product product) {
        this.product = product;
    }
    public member getMember() {
        return member;
    }

    public void setMember(member member) {
        this.member = member;
    }
    public Employee getEmployee() {
        return employee;
    }

    public void setEmployee(Employee employee) {
        this.employee = employee;
    }

}