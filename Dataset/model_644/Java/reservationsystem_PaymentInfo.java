




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class reservationsystem_PaymentInfo extends Booking {

    private String cardNo;
    private String id;
    private String cardAddr;
    private LocalDate createTime;
    private String cardOwner;
    private int type;
    private LocalDate payTime;
    private int status;





    private reservationsystem_Booking reservationsystem_booking;


    public reservationsystem_PaymentInfo(
        String cardNo,        String id,        String cardAddr,        LocalDate createTime,        String cardOwner,        int type,        LocalDate payTime,        int status    ) {
        super(
        );
        this.cardNo = cardNo;
        this.id = id;
        this.cardAddr = cardAddr;
        this.createTime = createTime;
        this.cardOwner = cardOwner;
        this.type = type;
        this.payTime = payTime;
        this.status = status;
    }


    public String getCardno() {
        return cardNo;
    }

    public void setCardno(String cardNo) {
        this.cardNo = cardNo;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getCardaddr() {
        return cardAddr;
    }

    public void setCardaddr(String cardAddr) {
        this.cardAddr = cardAddr;
    }
    public LocalDate getCreatetime() {
        return createTime;
    }

    public void setCreatetime(LocalDate createTime) {
        this.createTime = createTime;
    }
    public String getCardowner() {
        return cardOwner;
    }

    public void setCardowner(String cardOwner) {
        this.cardOwner = cardOwner;
    }
    public int getType() {
        return type;
    }

    public void setType(int type) {
        this.type = type;
    }
    public LocalDate getPaytime() {
        return payTime;
    }

    public void setPaytime(LocalDate payTime) {
        this.payTime = payTime;
    }
    public int getStatus() {
        return status;
    }

    public void setStatus(int status) {
        this.status = status;
    }

    public reservationsystem_Booking getReservationsystem_booking() {
        return reservationsystem_booking;
    }

    public void setReservationsystem_booking(reservationsystem_Booking reservationsystem_booking) {
        this.reservationsystem_booking = reservationsystem_booking;
    }

}