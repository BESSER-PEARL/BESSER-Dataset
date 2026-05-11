




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class test_TestModel  {

    private LocalDate birthDate;
    private String accountBalance;
    private String overdrawAccount;
    private String name;
    private String childCount;
    private String gender;
    private int age;
    private String isSelectable;





    private test_AddressModel test_addressmodel;


    public test_TestModel(
        LocalDate birthDate,        String accountBalance,        String overdrawAccount,        String name,        String childCount,        String gender,        int age,        String isSelectable    ) {
        this.birthDate = birthDate;
        this.accountBalance = accountBalance;
        this.overdrawAccount = overdrawAccount;
        this.name = name;
        this.childCount = childCount;
        this.gender = gender;
        this.age = age;
        this.isSelectable = isSelectable;
    }


    public LocalDate getBirthdate() {
        return birthDate;
    }

    public void setBirthdate(LocalDate birthDate) {
        this.birthDate = birthDate;
    }
    public String getAccountbalance() {
        return accountBalance;
    }

    public void setAccountbalance(String accountBalance) {
        this.accountBalance = accountBalance;
    }
    public String getOverdrawaccount() {
        return overdrawAccount;
    }

    public void setOverdrawaccount(String overdrawAccount) {
        this.overdrawAccount = overdrawAccount;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getChildcount() {
        return childCount;
    }

    public void setChildcount(String childCount) {
        this.childCount = childCount;
    }
    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }
    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }
    public String getIsselectable() {
        return isSelectable;
    }

    public void setIsselectable(String isSelectable) {
        this.isSelectable = isSelectable;
    }

    public test_AddressModel getTest_addressmodel() {
        return test_addressmodel;
    }

    public void setTest_addressmodel(test_AddressModel test_addressmodel) {
        this.test_addressmodel = test_addressmodel;
    }

}