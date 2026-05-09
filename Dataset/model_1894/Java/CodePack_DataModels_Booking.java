




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class CodePack_DataModels_Booking  {

    private String contact_name;
    private boolean isCheckedIn;
    private int id;
    private int customer_id;
    private String contact_email;
    private LocalDate date_check_in;
    private int bonus_points_used;
    private float total_price;
    private LocalDate date_check_out;
    private int payment_id;
    private int contact_phone;





    private Room room;


    public CodePack_DataModels_Booking(
        String contact_name,        boolean isCheckedIn,        int id,        int customer_id,        String contact_email,        LocalDate date_check_in,        int bonus_points_used,        float total_price,        LocalDate date_check_out,        int payment_id,        int contact_phone    ) {
        this.contact_name = contact_name;
        this.isCheckedIn = isCheckedIn;
        this.id = id;
        this.customer_id = customer_id;
        this.contact_email = contact_email;
        this.date_check_in = date_check_in;
        this.bonus_points_used = bonus_points_used;
        this.total_price = total_price;
        this.date_check_out = date_check_out;
        this.payment_id = payment_id;
        this.contact_phone = contact_phone;
    }


    public String getContact_name() {
        return contact_name;
    }

    public void setContact_name(String contact_name) {
        this.contact_name = contact_name;
    }
    public boolean getIscheckedin() {
        return isCheckedIn;
    }

    public void setIscheckedin(boolean isCheckedIn) {
        this.isCheckedIn = isCheckedIn;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public int getCustomer_id() {
        return customer_id;
    }

    public void setCustomer_id(int customer_id) {
        this.customer_id = customer_id;
    }
    public String getContact_email() {
        return contact_email;
    }

    public void setContact_email(String contact_email) {
        this.contact_email = contact_email;
    }
    public LocalDate getDate_check_in() {
        return date_check_in;
    }

    public void setDate_check_in(LocalDate date_check_in) {
        this.date_check_in = date_check_in;
    }
    public int getBonus_points_used() {
        return bonus_points_used;
    }

    public void setBonus_points_used(int bonus_points_used) {
        this.bonus_points_used = bonus_points_used;
    }
    public float getTotal_price() {
        return total_price;
    }

    public void setTotal_price(float total_price) {
        this.total_price = total_price;
    }
    public LocalDate getDate_check_out() {
        return date_check_out;
    }

    public void setDate_check_out(LocalDate date_check_out) {
        this.date_check_out = date_check_out;
    }
    public int getPayment_id() {
        return payment_id;
    }

    public void setPayment_id(int payment_id) {
        this.payment_id = payment_id;
    }
    public int getContact_phone() {
        return contact_phone;
    }

    public void setContact_phone(int contact_phone) {
        this.contact_phone = contact_phone;
    }

    public Room getRoom() {
        return room;
    }

    public void setRoom(Room room) {
        this.room = room;
    }

}