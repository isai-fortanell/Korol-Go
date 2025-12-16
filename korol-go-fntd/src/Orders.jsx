import { useState, useEffect, } from "react";
import "./Orders.css"
import React from "react";

const OrderCard = (props) => {
  return <div className="order-card">
          <div className="order-header">
            <h1 className="order_name">{props.name}</h1>
            <h1 className="order_client">From {props.client}</h1> 
          </div>
          {/* <h1>Order {props.number}</h1> */}
          <div className="order-body">
            <p className="order_time">Ordered: {props.time}</p>
            <h1 className="order_delivered">{props.delivered ? "Delivered":"Not delivered"}</h1>  
          </div>
        </div>;
};

// ViewROders

export function ViewOrders() {
  let [users, setUsers] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const webResponse = await fetch("/view-orders-json/");
        const jsonResponse = await webResponse.json();
        setUsers(jsonResponse);
      } catch (error) {
        console.log("%c>> ERROR-APLICATION: [DURING ORDERS FETCHING] \n", "color: #F32424", error);
      }
    };

    fetchData();
  }, []);

  return (
    <div id="order-cards_inner">
      {users.map((user, key) => (
        <OrderCard key={key} number={user.number} client={user.client} name={user.name} time={user.time} delivered={user.delivered} />
        ))}
    </div>
  );
}
