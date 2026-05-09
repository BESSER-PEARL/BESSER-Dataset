





import java.util.List;
import java.util.ArrayList;

public class BankingSystem_Customer  {

    private String name;
    private String customerType;
    private String phoneNumber;
    private String address;
    private int age;





    private BankingSystem_Branch bankingsystem_branch;




    private BankingSystem_Branch bankingsystem_branch;


    public BankingSystem_Customer(
        String name,        String customerType,        String phoneNumber,        String address,        int age    ) {
        this.name = name;
        this.customerType = customerType;
        this.phoneNumber = phoneNumber;
        this.address = address;
        this.age = age;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getCustomertype() {
        return customerType;
    }

    public void setCustomertype(String customerType) {
        this.customerType = customerType;
    }
    public String getPhonenumber() {
        return phoneNumber;
    }

    public void setPhonenumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public BankingSystem_Branch getBankingsystem_branch() {
        return bankingsystem_branch;
    }

    public void setBankingsystem_branch(BankingSystem_Branch bankingsystem_branch) {
        this.bankingsystem_branch = bankingsystem_branch;
    }
    public BankingSystem_Branch getBankingsystem_branch() {
        return bankingsystem_branch;
    }

    public void setBankingsystem_branch(BankingSystem_Branch bankingsystem_branch) {
        this.bankingsystem_branch = bankingsystem_branch;
    }

}