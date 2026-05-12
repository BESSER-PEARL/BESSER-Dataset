





import java.util.List;
import java.util.ArrayList;

public class Order  {

    private String TotalPrice;
    private String CodeId;
    private String Name;
    private String Address;
    private String UserId;
    private String Comment;
    private int Status;
    private String PhoneNumber;
    private String Email;





    private OrderItem orderitem;




    private CouponCode couponcode;


    public Order(
        String TotalPrice,        String CodeId,        String Name,        String Address,        String UserId,        String Comment,        int Status,        String PhoneNumber,        String Email    ) {
        this.TotalPrice = TotalPrice;
        this.CodeId = CodeId;
        this.Name = Name;
        this.Address = Address;
        this.UserId = UserId;
        this.Comment = Comment;
        this.Status = Status;
        this.PhoneNumber = PhoneNumber;
        this.Email = Email;
    }


    public String getTotalprice() {
        return TotalPrice;
    }

    public void setTotalprice(String TotalPrice) {
        this.TotalPrice = TotalPrice;
    }
    public String getCodeid() {
        return CodeId;
    }

    public void setCodeid(String CodeId) {
        this.CodeId = CodeId;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }
    public String getUserid() {
        return UserId;
    }

    public void setUserid(String UserId) {
        this.UserId = UserId;
    }
    public String getComment() {
        return Comment;
    }

    public void setComment(String Comment) {
        this.Comment = Comment;
    }
    public int getStatus() {
        return Status;
    }

    public void setStatus(int Status) {
        this.Status = Status;
    }
    public String getPhonenumber() {
        return PhoneNumber;
    }

    public void setPhonenumber(String PhoneNumber) {
        this.PhoneNumber = PhoneNumber;
    }
    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }

    public OrderItem getOrderitem() {
        return orderitem;
    }

    public void setOrderitem(OrderItem orderitem) {
        this.orderitem = orderitem;
    }
    public CouponCode getCouponcode() {
        return couponcode;
    }

    public void setCouponcode(CouponCode couponcode) {
        this.couponcode = couponcode;
    }

}