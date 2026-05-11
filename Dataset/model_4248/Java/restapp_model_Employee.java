




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class restapp_model_Employee  {

    private String mobile;
    private String phone;
    private boolean working;
    private float salary;
    private float comission;
    private String rg;
    private int id;
    private String zipcode;
    private String name;
    private String address;
    private int status;
    private String cpf;
    private LocalDate fired;
    private LocalDate contracted;



    public restapp_model_Employee(
        String mobile,        String phone,        boolean working,        float salary,        float comission,        String rg,        int id,        String zipcode,        String name,        String address,        int status,        String cpf,        LocalDate fired,        LocalDate contracted    ) {
        this.mobile = mobile;
        this.phone = phone;
        this.working = working;
        this.salary = salary;
        this.comission = comission;
        this.rg = rg;
        this.id = id;
        this.zipcode = zipcode;
        this.name = name;
        this.address = address;
        this.status = status;
        this.cpf = cpf;
        this.fired = fired;
        this.contracted = contracted;
    }


    public String getMobile() {
        return mobile;
    }

    public void setMobile(String mobile) {
        this.mobile = mobile;
    }
    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }
    public boolean getWorking() {
        return working;
    }

    public void setWorking(boolean working) {
        this.working = working;
    }
    public float getSalary() {
        return salary;
    }

    public void setSalary(float salary) {
        this.salary = salary;
    }
    public float getComission() {
        return comission;
    }

    public void setComission(float comission) {
        this.comission = comission;
    }
    public String getRg() {
        return rg;
    }

    public void setRg(String rg) {
        this.rg = rg;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getZipcode() {
        return zipcode;
    }

    public void setZipcode(String zipcode) {
        this.zipcode = zipcode;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public int getStatus() {
        return status;
    }

    public void setStatus(int status) {
        this.status = status;
    }
    public String getCpf() {
        return cpf;
    }

    public void setCpf(String cpf) {
        this.cpf = cpf;
    }
    public LocalDate getFired() {
        return fired;
    }

    public void setFired(LocalDate fired) {
        this.fired = fired;
    }
    public LocalDate getContracted() {
        return contracted;
    }

    public void setContracted(LocalDate contracted) {
        this.contracted = contracted;
    }


}