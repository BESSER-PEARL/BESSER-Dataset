




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class shop_ChequePayment extends Payment {

    private boolean deposited;
    private LocalDate depositDate;



    public shop_ChequePayment(
        boolean deposited,        LocalDate depositDate    ) {
        super(
        );
        this.deposited = deposited;
        this.depositDate = depositDate;
    }


    public boolean getDeposited() {
        return deposited;
    }

    public void setDeposited(boolean deposited) {
        this.deposited = deposited;
    }
    public LocalDate getDepositdate() {
        return depositDate;
    }

    public void setDepositdate(LocalDate depositDate) {
        this.depositDate = depositDate;
    }


}