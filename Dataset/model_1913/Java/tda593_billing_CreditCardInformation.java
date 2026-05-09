




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class tda593_billing_CreditCardInformation  {

    private String ccv;
    private String lastName;
    private String firstName;
    private LocalDate expirationDate;
    private String cardNumber;





    private booking_LegalEntity booking_legalentity;


    public tda593_billing_CreditCardInformation(
        String ccv,        String lastName,        String firstName,        LocalDate expirationDate,        String cardNumber    ) {
        this.ccv = ccv;
        this.lastName = lastName;
        this.firstName = firstName;
        this.expirationDate = expirationDate;
        this.cardNumber = cardNumber;
    }


    public String getCcv() {
        return ccv;
    }

    public void setCcv(String ccv) {
        this.ccv = ccv;
    }
    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
    }
    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }
    public LocalDate getExpirationdate() {
        return expirationDate;
    }

    public void setExpirationdate(LocalDate expirationDate) {
        this.expirationDate = expirationDate;
    }
    public String getCardnumber() {
        return cardNumber;
    }

    public void setCardnumber(String cardNumber) {
        this.cardNumber = cardNumber;
    }

    public booking_LegalEntity getBooking_legalentity() {
        return booking_legalentity;
    }

    public void setBooking_legalentity(booking_LegalEntity booking_legalentity) {
        this.booking_legalentity = booking_legalentity;
    }

}