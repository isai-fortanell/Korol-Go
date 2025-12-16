import React from "react";
import ReactDOM from "react-dom/client";
import { ViewOrders } from "./Orders.jsx";

// const viewOrders = document.getElementById("order-cards_container");
// if (viewOrders) {
//   ReactDOM.render(<ViewOrders />, viewOrders);
// }

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <div>
    <ViewOrders />
  </div>
);
