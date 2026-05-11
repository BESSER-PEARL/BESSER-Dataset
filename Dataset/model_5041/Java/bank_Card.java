




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class bank_Card extends Device {

    private String id;
    private LocalDate activated;
    private LocalDate issued;
    private LocalDate expires;
    private boolean virtual;
    private LocalDate deactivated;





    private bank_Merchant bank_merchant;




    private bank_Card bank_card;


    public bank_Card(
        String id,        LocalDate activated,        LocalDate issued,        LocalDate expires,        boolean virtual,        LocalDate deactivated    ) {
        super(
        );
        this.id = id;
        this.activated = activated;
        this.issued = issued;
        this.expires = expires;
        this.virtual = virtual;
        this.deactivated = deactivated;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public LocalDate getActivated() {
        return activated;
    }

    public void setActivated(LocalDate activated) {
        this.activated = activated;
    }
    public LocalDate getIssued() {
        return issued;
    }

    public void setIssued(LocalDate issued) {
        this.issued = issued;
    }
    public LocalDate getExpires() {
        return expires;
    }

    public void setExpires(LocalDate expires) {
        this.expires = expires;
    }
    public boolean getVirtual() {
        return virtual;
    }

    public void setVirtual(boolean virtual) {
        this.virtual = virtual;
    }
    public LocalDate getDeactivated() {
        return deactivated;
    }

    public void setDeactivated(LocalDate deactivated) {
        this.deactivated = deactivated;
    }

    public bank_Merchant getBank_merchant() {
        return bank_merchant;
    }

    public void setBank_merchant(bank_Merchant bank_merchant) {
        this.bank_merchant = bank_merchant;
    }
    public bank_Card getBank_card() {
        return bank_card;
    }

    public void setBank_card(bank_Card bank_card) {
        this.bank_card = bank_card;
    }

}