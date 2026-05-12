





import java.util.List;
import java.util.ArrayList;

public class Apartment  {

    private int securityDeposit;
    private int monthlyRent;
    private int lease;
    private int size;



    public Apartment(
        int securityDeposit,        int monthlyRent,        int lease,        int size    ) {
        this.securityDeposit = securityDeposit;
        this.monthlyRent = monthlyRent;
        this.lease = lease;
        this.size = size;
    }


    public int getSecuritydeposit() {
        return securityDeposit;
    }

    public void setSecuritydeposit(int securityDeposit) {
        this.securityDeposit = securityDeposit;
    }
    public int getMonthlyrent() {
        return monthlyRent;
    }

    public void setMonthlyrent(int monthlyRent) {
        this.monthlyRent = monthlyRent;
    }
    public int getLease() {
        return lease;
    }

    public void setLease(int lease) {
        this.lease = lease;
    }
    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }


}