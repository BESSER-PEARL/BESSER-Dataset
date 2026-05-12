





import java.util.List;
import java.util.ArrayList;

public class price_quote  {

    private String _bulk_rate_price;





    private _supplier _supplier;




    private Part part;


    public price_quote(
        String _bulk_rate_price    ) {
        this._bulk_rate_price = _bulk_rate_price;
    }


    public String get_bulk_rate_price() {
        return _bulk_rate_price;
    }

    public void set_bulk_rate_price(String _bulk_rate_price) {
        this._bulk_rate_price = _bulk_rate_price;
    }

    public _supplier get_supplier() {
        return _supplier;
    }

    public void set_supplier(_supplier _supplier) {
        this._supplier = _supplier;
    }
    public Part getPart() {
        return part;
    }

    public void setPart(Part part) {
        this.part = part;
    }

}