




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Booking_Entity  {

    private LocalDate CheckInDate;
    private String phone;
    private int NoOfDays;
    private String address;
    private String email;



    public Booking_Entity(
        LocalDate CheckInDate,        String phone,        int NoOfDays,        String address,        String email    ) {
        this.CheckInDate = CheckInDate;
        this.phone = phone;
        this.NoOfDays = NoOfDays;
        this.address = address;
        this.email = email;
    }


    public LocalDate getCheckindate() {
        return CheckInDate;
    }

    public void setCheckindate(LocalDate CheckInDate) {
        this.CheckInDate = CheckInDate;
    }
    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }
    public int getNoofdays() {
        return NoOfDays;
    }

    public void setNoofdays(int NoOfDays) {
        this.NoOfDays = NoOfDays;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }


}