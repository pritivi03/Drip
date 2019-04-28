//
//  IrrigationViewController.swift
//  Drip
//
//  Created by Pritivi Rajkumar on 4/28/19.
//  Copyright © 2019 Pritivi Rajkumar. All rights reserved.
//

import UIKit

class IrrigationViewController: ViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        DispatchQueue.main.asyncAfter(deadline: .now() + 1.0, execute: {
            let myUrl = NSURL(string: "https://drip--abhinavkolli1.repl.co/switch");
            
            // Creaste URL Request
            let request = NSMutableURLRequest(url:myUrl! as URL);
            
            request.httpMethod = "GET"
            
            let task = URLSession.shared.dataTask(with: request as URLRequest) {
                data, response, error in
               
                print("did request")
                
            }
            
            task.resume()
        })
    }
    

    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destination.
        // Pass the selected object to the new view controller.
    }
    */

}
