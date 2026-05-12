





import java.util.List;
import java.util.ArrayList;

public class RadixClient  {

    private None state;
    private String password;
    private String redisUrl;





    private ShoppingCart shoppingcart;




    private RedisStateStore redisstatestore;


    public RadixClient(
        None state,        String password,        String redisUrl    ) {
        this.state = state;
        this.password = password;
        this.redisUrl = redisUrl;
    }


    public None getState() {
        return state;
    }

    public void setState(None state) {
        this.state = state;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getRedisurl() {
        return redisUrl;
    }

    public void setRedisurl(String redisUrl) {
        this.redisUrl = redisUrl;
    }

    public ShoppingCart getShoppingcart() {
        return shoppingcart;
    }

    public void setShoppingcart(ShoppingCart shoppingcart) {
        this.shoppingcart = shoppingcart;
    }
    public RedisStateStore getRedisstatestore() {
        return redisstatestore;
    }

    public void setRedisstatestore(RedisStateStore redisstatestore) {
        this.redisstatestore = redisstatestore;
    }

}